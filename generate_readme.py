#!/usr/bin/env python3
import os
import glob
import re
from pathlib import Path

def extract_frontmatter(content):
    """Extract frontmatter from markdown file"""
    if not content.startswith('---'):
        return {}
    
    try:
        end_idx = content.find('---', 3)
        if end_idx == -1:
            return {}
        
        frontmatter = content[3:end_idx].strip()
        metadata = {}
        
        for line in frontmatter.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                metadata[key] = value
        
        return metadata
    except:
        return {}

def get_guides_by_category():
    """Get all guides organized by category directories"""
    guides_dir = "/Users/mahyoussef/repos/In-a-Nutshell/guides"
    categories = {}
    
    # Get all directories (categories)
    for category_dir in sorted(os.listdir(guides_dir)):
        category_path = os.path.join(guides_dir, category_dir)
        
        if not os.path.isdir(category_path) or category_dir == 'images':
            continue
        
        # Clean up category name for display
        category_name = category_dir.replace('-', ' ').title()
        category_name = category_name.replace('Ai ', 'AI ').replace('Cicd', 'CI/CD')
        category_name = category_name.replace('Apis', 'APIs')
        
        guides = []
        
        # Get all .md files in this category
        for md_file in glob.glob(os.path.join(category_path, '*.md')):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                metadata = extract_frontmatter(content)
                file_name = os.path.basename(md_file)
                
                # Create guide entry
                guide = {
                    'title': metadata.get('title', file_name.replace('.md', '').replace('-', ' ').title()),
                    'excerpt': metadata.get('excerpt', ''),
                    'file_path': f"guides/{category_dir}/{file_name}",
                    'file_name': file_name
                }
                
                guides.append(guide)
            
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
        
        if guides:
            # Sort guides by title
            guides.sort(key=lambda x: x['title'])
            categories[category_name] = guides
    
    return categories

def generate_readme_content():
    """Generate the complete README.md content"""
    categories = get_guides_by_category()
    
    # Header content
    header = '''<div style="direction: rtl;">
<p>
  <a href="https://eqraatech.com/"><img src="images/guides-banner1.png" /> </a>
</p>

  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/eqraatechcom/)
  [![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/eqraatechcom)
  [![Eqraatech](https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://eqraatech.com/)
  [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40Eqraatechcom)](https://twitter.com/Eqraatechcom)

  [![Buy Me Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/mahyoussef)
  [![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/mahyoussef)
  [![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/mahyoussef97)

  
# ورقة وقلم 🚀
محتوى تقني متميز في مختلف مجالات هندسة البرمجيات عن طريق تبسيط المفاهيم البرمجية المعقدة بشكل سلس وباستخدام صور توضيحية مذهلة

<p>
  <img src="images/pen-paper.png" style="width: 640px">
</p>

# فهرس المواضيع 🌠
'''
    
    # Generate table of contents
    toc = []
    content_sections = []
    
    for category_name, guides in categories.items():
        # Add category to TOC
        category_anchor = category_name.lower().replace(' ', '-').replace('/', '-').replace('&', 'and')
        toc.append(f"- [{category_name}](#{category_anchor})")
        
        # Add guides to TOC as sub-items
        for guide in guides:
            guide_anchor = guide['title'].lower().replace(' ', '-').replace('/', '-').replace('&', 'and')
            guide_anchor = re.sub(r'[^a-z0-9\-]', '', guide_anchor)
            toc.append(f"  - [{guide['title']}](#{guide_anchor})")
        
        # Generate content section
        section = f"\n## {category_name}\n\n"
        
        for guide in guides:
            guide_anchor = guide['title'].lower().replace(' ', '-').replace('/', '-').replace('&', 'and')
            guide_anchor = re.sub(r'[^a-z0-9\-]', '', guide_anchor)
            
            section += f"### {guide['title']}\n"
            if guide['excerpt']:
                section += f"{guide['excerpt']}\n\n"
            
            section += f"📄 **[اقرأ المقال]({guide['file_path']})**\n\n"
            section += "---\n\n"
        
        content_sections.append(section)
    
    # Combine everything
    full_content = header
    full_content += '\n'.join(toc)
    full_content += '\n\n'
    full_content += ''.join(content_sections)
    
    # Add footer
    footer = '''\n## المساهمة 🤝

نرحب بمساهماتكم في تطوير المحتوى! يمكنكم:
- إضافة مواضيع جديدة
- تحسين المحتوى الموجود
- الإبلاغ عن الأخطاء
- اقتراح تحسينات

## الدعم 💖

إذا أعجبكم المحتوى، يمكنكم دعمنا من خلال:
- ⭐ إعطاء نجمة للمشروع
- 🔄 مشاركة المحتوى
- ☕ شراء قهوة للفريق

## الترخيص 📝

هذا المشروع مرخص تحت رخصة MIT - راجعوا ملف [LICENSE](LICENSE) لمزيد من التفاصيل.

---

<div align="center">
  <p>صنع بـ ❤️ من فريق إقرأ تك</p>
  <p><a href="https://eqraatech.com">eqraatech.com</a></p>
</div>'''
    
    full_content += footer
    
    return full_content

def main():
    """Main function to generate and write the README"""
    print("Generating README.md...")
    
    readme_content = generate_readme_content()
    
    # Write to README.md in the root directory
    readme_path = "/Users/mahyoussef/repos/In-a-Nutshell/README.md"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"README.md generated successfully!")
    print(f"Total categories processed: {len(get_guides_by_category())}")
    
    # Count total guides
    total_guides = sum(len(guides) for guides in get_guides_by_category().values())
    print(f"Total guides included: {total_guides}")

if __name__ == '__main__':
    main()


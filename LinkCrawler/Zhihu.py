import requests
from bs4 import BeautifulSoup


def process_inline_code(element):
    """Replace HTML <code> tags with markdown inline code format."""
    code_tags = element.find_all('code', recursive=False)
    for code_tag in code_tags:
        code_content = code_tag.get_text()
        markdown_code = f"`{code_content}`"
        code_tag.replace_with(markdown_code)


def save_as_markdown(tag, file):
    """Convert specific HTML tags to markdown format and save them."""
    process_inline_code(tag)
    if tag.name == 'h2':
        file.write('## ' + tag.get_text() + '\n')
    elif tag.name == 'h3':
        file.write('### ' + tag.get_text() + '\n')
    elif tag.name == 'p':
        file.write(tag.get_text() + '\n\n')
    elif tag.name == 'ol':
        index = 0
        for idx, li in enumerate(tag.find_all('li', recursive=False), start=1):
            index += 1
            file.write(f'{index}. ' + li.get_text() + '\n')
    elif tag.name == 'div' and tag.code:
        language = tag.code.get('class')[0].replace('language-', '') if tag.code.get('class') else ''
        file.write(f'```{language}\n' + tag.code.get_text() + '```\n')


def zhihu_article(url):
    """Fetch and save the content of a Zhihu article as a markdown file."""
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='Post-Main Post-NormalMain')

    relevant_tags = ['h2', 'h3', 'p', 'ol', 'li', 'div']  # List all tags you want to process

    with open('output.md', 'w', encoding='utf-8') as file:
        for article in articles:
            for tag in article.find_all(relevant_tags):
                save_as_markdown(tag, file)


def ZhihuArticle(url):
    zhihu_article(url)

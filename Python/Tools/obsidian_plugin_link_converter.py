link_templates = ["https://obsidian.md/plugins?id=", "obsidian://show-plugin?id="]


def convert_obsidian_link(link):
    id = link.split("?id=")[1]
    converted_links = []
    for template in link_templates:
        if template not in link:
            converted_links.append(template + id)
    return converted_links


if __name__ == '__main__':
    for link in convert_obsidian_link(input('URL: ')):
        print(link)

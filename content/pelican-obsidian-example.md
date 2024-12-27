---
title: Pelican Obsidian Example
date: 2015-11-01 00:35
author: pelican
category: Example
tags:
  - pelican
  - obsidian
  - plugin
  - markdown
slug: pelican-obsidian-example
cover: /assets/images/pelican-obsidian-example-cover.webp
color: gray
headline: This blog post written in Obsidian and published with Pelican
status: published
---

This blog post written in Obsidian and published with Pelican.

Used [https://github.com/jonathan-s/pelican-obsidian](pelican-obsidian) plugin to convert Obsidian markdown to Pelican markdown.

Obsidian is a powerful knowledge base that works on top of a local folder of plain text Markdown files. Here are some key Markdown features in Obsidian:

## Headings

Use `#` for headings. The number of `#` symbols indicates the level of the heading.

```md
# Heading 1
## Heading 2
### Heading 3
```
# Heading 1
## Heading 2
### Heading 3

## Bold and Italics:

Use `**` or `__` for bold text and `*` or `_` for italic text.

```md
**bold text**

*italic text*
```

**bold text**

*italic text*

## Lists

Create ordered and unordered lists using numbers or `-`/`*`.

```md
- Item 1
- Item 2
    - Subitem 1
1. First item
2. Second item
```

- Item 1
- Item 2
    - Subitem 1
1. First item
2. Second item

## Links

Create links using `text`.

```
[Obsidian](https://obsidian.md)
```
[Obsidian](https://obsidian.md)

Internal links to other notes in Obsidian are created using `[[note title]]`.

```
Refer this blog post [[code-block-markdown]]
```

Refer this blog post [[code-block-markdown]]


## Images

Embed images using `![alt text](image URL)`.

Image from public URL

```
![Obsidian Logo](https://upload.wikimedia.org/wikipedia/commons/1/10/2023_Obsidian_logo.svg)
```

![Obsidian Logo](https://upload.wikimedia.org/wikipedia/commons/1/10/2023_Obsidian_logo.svg)


Image from local file

```
![[pelican-in-rock.png]]
```

![[pelican-in-rock.png]]

## Code Blocks

Use backticks for inline code and triple backticks for code blocks.

```md
`inline code`
```

`inline code`

Multiline code block:

```md
```python
def hello_world():
    print("Hello, World!")
```
```

```python
def hello_world():
    print("Hello, World!")
```

## Blockquotes

Use `>` for blockquotes.

```md
> This is a blockquote.
```

> This is a blockquote.

## Tables

Create tables using pipes `|` and dashes `-`.

```md
| Header 1 | Header 2 |
|----------|----------|
| Row 1    | Data 1   |
| Row 2    | Data 2   |
```

| Header 1 | Header 2 |
|----------|----------|
| Row 1    | Data 1   |
| Row 2    | Data 2   |

These are just a few of the many Markdown features supported by Obsidian. It also supports advanced features like backlinks, graph view, and plugins to extend its functionality.

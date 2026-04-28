from docling.document_converter import DocumentConverter

converter = DocumentConverter()

# Convertendo um pdf para markdown
# result = converter.convert("./2408.09869v5.pdf")

# Convertendo uma url para markdown
# result = converter.convert("https://arxiv.org/pdf/2408.09869")

# Convertendo html para markdown
result = converter.convert("https://docling-project.github.io/docling/")

document = result.document
markdown_output = document.export_to_markdown()

print(markdown_output)


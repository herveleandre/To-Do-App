contents = ["carrots slices", "Oranges slices", "Peach slices"]

filenames = ["doc.txt", "Report.txt", "Presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", "w")
    file.write(content)

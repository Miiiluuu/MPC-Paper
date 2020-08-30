import subprocess
import glob
import staplelib.stapler as stapler
import os

stapler.main(["split", "paper.pdf", "--force", "--destdir", "bilder"])
pdfpages = glob.glob("bilder/*.pdf")
for page in pdfpages:
    subprocess.run(["poppler-0.68.0/bin/pdftocairo.exe", page, "-svg"])
    os.remove(page)

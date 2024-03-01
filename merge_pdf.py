import pypdf

merger = pypdf.PdfMerger()

merger.append('pdf/recipe_0000001263.pdf')
merger.append('pdf/recipe_0000001337.pdf')
merger.append('pdf/recipe_0000001491.pdf')

merger.write('pdf/recipe.pdf')
merger.close()
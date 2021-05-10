import pandas as pd
from gutenberg.acquire import load_etext
from gutenberg.query import get_metadata
from gutenberg.cleanup import strip_headers
from top_1k import book_list
from gutenberg._domain_model.exceptions import UnknownDownloadUriException
import chapterize

# from gutenberg.acquire import get_metadata_cache
# cache = get_metadata_cache()
# cache.populate()


# text = strip_headers(load_etext(2701)).strip()
# print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'

df = pd.DataFrame(columns=['book_num', 'title', 'author'])
books = []
authors = []
titles = []

# this utilizes creating lists before appending to the df
# good use of avoiding the quadratic copy
# https://stackoverflow.com/questions/37009287/using-pandas-append-within-for-loop/37009561#37009561
for book in book_list:
	try: 
		## get actual books
		# text = strip_headers(load_etext(book)).strip()
		# print(text,  file=open(str(book) + '.txt', 'w'))

		# df['book_num'] = str(book)
		# df = df.append({'book_num': str(book)}, ignore_index=True)
		books.append(str(book))
		# print(list(get_metadata('title', book)))
		try:
			titles.append(str(list(get_metadata('title', book))[0]))
			# df = df.append({'title': str(list(get_metadata('title', book))[0])})
			# df['title'] = str(list(get_metadata('title', book))[0])
			# print(df['title'])
		except IndexError:
			titles.append('N/A')
			# df = df.append({'title': 'N/A'})
			# df['title'] = 'N/A'
		try:
			authors.append(str(list(get_metadata('author', book))[0]))
			# df['author'] = str(list(get_metadata('author', book))[0])
			# df = df.append({'author': str(list(get_metadata('author', book))[0])})
		except IndexError:
			authors.append('N/A')
			# df['author'] = 'N/A'
			# df = df.append({'author': 'N/A'})
		# print(df)
	except UnknownDownloadUriException:
		continue
	except Exception:
		raise Exception

df = pd.DataFrame({'book_num': books, 'title': titles, 'author': authors})
df.to_csv('book_metadata.csv', mode='a')
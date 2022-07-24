# NeurocessTasks

--TASK 1 --

In this part, some values were changed according to the given hierarchy in names.json file.
data.pkl pickle file contains a 3 column dataframe in which these columns are “c1” , “c2” and “task”.
The last column, whose name is “task” contains 0 and 1 values. These 0 and 1 values are placed as a group 
which is shown in the table. Task values were changed according to the values in names.json file

After editing these values, the repetition of the names under 'task' column has been conted. 
Lastly, the counted values were shown in a bar graph. The x-axis is counted names and 
the y-axis is the count valuesof these names.

-- TASK 2 --

In this part, I've built a simple API and scrape amazon page.

Page Link:

https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1
%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5
%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=ap
pl%2Caps%2C122&ref=sr_nr_n_4

In the web scraping part, the name and price data of listed products were scraped.
Finally, my flask API system takes these scraped name and prices data and show
them on a local webpage.

The chromedriver is used for version 103, compatible with my own chrome driver on my PC

The scraped data is consist of maximum 27 items, and seen in json format
Since the scraped material is in Turkish, some unique Turkish characters (e.g 'ç,i,ü,ğ,İ,..')
are not in range of ascii characters therefore json output contains values like:
"Jabra Elite 3 Kulak ic\u0327i Kablosuz Bluetooth Kulakl\u0131k"

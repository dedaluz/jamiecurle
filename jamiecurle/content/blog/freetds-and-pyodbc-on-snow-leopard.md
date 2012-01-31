title: "FreeTDS + pyodbc on Snow Leopard"
description: "A project required pulling data from a MSSQL server into MySQL. It was a world of pain."
created: 2010-11-19 14:20:43
---

I spent a long, long time trying to get FreeTDS to play nice with with pyodbc, but everytime I tried to connect I was met with the same fateful message

<code lang="python">
pyodbc.Error: ('08S01', '[08S01] [FreeTDS][SQL Server]Unable to connect: Adaptive Server is unavailable or does not exist (20009) (SQLDriverConnectW)')
</code>

I tried my [bulletproof troubleshooting steps](/blog/4-Bulletproof-Troubleshooting) It was plugged & switched on and I'd checked. Many times, using many different methods.

Nothing was working. Then I came across a post entitled [mssql + freetds + pyodbc"](http://meantheory.wordpress.com/2009/10/01/mssql-freetds-pyodbc-snow-leopard).  It turns out that I needed to compile freetds explicitly setting the TDS Server version. 

<code lang="bash">
./configure --prefix=/usr/local/freetds --with-iodbc=/usr --with-tdsver=8.0
</code>

Then the usual make & make install

<code lang="bash">
make
sudo make install
</code>

Finally, before my eyes I saw a waterfall of ID's pouring out from the terminal. It was the most beautiful stdout I'd ever seen.

Thankyou [meantheory](http://meantheory.wordpress.com/)


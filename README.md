Money Maker
===========

Do you want to make some BTC quick?

This bot will help you to achieve it :)

WTF??? You talking shit dude!?
------------------------------
Nope. As you may know there's runcpa advertising cost per action network.

And now they have offer with hashflare.io. They give you about $0.2 just for a
user with verified email address.

So...
-----
As you may notice, we could just write a bot which will register on hashflare.io
and will verify addresses to make money. But there's some thing you need to
know: runcpa has it's "skynet" system which identifies fraud traffic. But it's
not working good (as Google Adsense, for example).

And idea is...
--------------
And idea is to have DB with your "hashflare users" and make, maybe, two or three
10GH buy per 100 users. So, in ideal world the formula is ```n * ($0.2 - 0.03 *
$1.6)```, as $1.6 - it's 10GH price at hashflare, `n` is quantity of your "users",
$0.2 - price for a user verification and 0.03 - it's a 3% :)

So the idea is to make about 3% of sales to users to get money :) But not so
many, I guess. For me, the bot verified users for a 0.49BTC (for a night), but
there were no sales at all. And now that account is "under investigation". So,
I've realized I need to make my "traffic quality" on 5%-9% so I will not get
banned. Also I need to say after that 0.49BTC night my IPs are getting "browser
checking" on cloudflare (hashflare uses it).

So the next day I've made about 0.07BTC, did 3 "sales" and my IPs on hashflare
got banned XD

And I don't want to buy new VPS and look for working SOCS5 proxies (tor isn't
working well) and I give these scripts to you :)

What do I need?
---------------
You need python3 installed on your machine. Also you need PostgreSQL installed,
as we need to store users somewhere. Yeah, PostgreSQL is so big for this you
say, and my answer is - "YEAH". You could use whatever you want like plain text
file, sqlite and so on. If you want to run, for example, Firefox, on virtual
display (on Linux), you need to install virtual framebuffer, for Fedora it will be

`$ sudo dnf install xorg-x11-server-Xvfb`

Next, you need to clone this repo somewhere:

`$ git clone https://github.com/slaykovsky/money_maker.git && cd money_maker`

And install requirements:

`$ pip install -r requirements.txt`

Then you need to register at https://runcpa.com. After registration, you need
to verify your email (email **MUST** be reachable for you because when you
will withdraw your money there will be verification email). Then you need to
search for a hashflare.io offer there. Accept it and there will be refferal
links. You need to have link which is **exactly** leading you to [this
page](http://profit.hashflare.eu/en/?utm_source=runcpa&utm_medium=cpa&utm_campaign=enlpprofit). Refferal link is starting by the `https://runcpa.com/getoffer`.

Next you need to add this string to a script as REFFERAL_LINK string constant.
And start the script :)

When you feel you need to "make a sale", you need to get email and password from
your DB and go to hashflare site. Than you need to login, and buy 10GH, for
example. When you make your sale, your traffic quality will be better and you
could withdraw your money.

WOW THX MATE IT WORKED
----------------------
In case it worked for you don't hesitate to make me some donation :)

BTC: 3JKTWQ8iis8rpkRnyuo1fa17g3YvqDH2sf

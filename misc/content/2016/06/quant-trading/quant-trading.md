Status: published
Date: 2016-06-09 19:32:27
Author: Ben Chuanlong Du
Slug: quant-trading
Title: Quant Trading
Category: Finance
Tags: quant, quantitative, trading, investment, money, stock, ETF, Alpaca, QuantConnect, QuantRocket
Modified: 2024-09-11 17:20:47

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://www.quantstart.com/

https://github.com/edtechre/pybroker

https://github.com/whittlem/pycryptobot

https://github.com/asavinov/intelligent-trading-bot

## Forums & Discussions

- [ML-Quant](https://www.ml-quant.com/public)

## Quant Trading Libraries

## General 

1. [RustQuant](https://github.com/avhz/RustQuant)
    is a Rust library for quantitative finance.

2. [zvt](https://github.com/zvtvz/zvt)
    is a modular quant framework.

### Technical Analysis

1. [TA-Lib](https://github.com/TA-Lib/ta-lib)
    is an open-source technical analysis library for financial applications. 
    It provides a wide range of technical indicators and functions for analyzing financial market data.

2. [QuantLib](https://github.com/lballabio/quantlib)
    is aimed at providing a comprehensive software framework for quantitative finance. 
    QuantLib is a free/open-source library for modeling, trading, and risk management in real-life.

3. [ffn](https://github.com/pmorissette/ffn)
    is a library that contains many useful functions 
    for those who work in quantitative finance. 
    It stands on the shoulders of giants (Pandas, Numpy, Scipy, etc.) 
    and provides a vast array of utilities, 
    from performance measurement and evaluation to graphing and common data transformations.

4. [riskparity.py](https://github.com/convexfi/riskparity.py)
    riskparityportfolio provides solvers to design risk parity portfolios. 
    In its simplest form, we consider the convex formulation with a unique solution proposed by Spinu (2013) and use cyclical methods inspired by Griveau-Billion et al. (2013) and Choi & Chen (2022). 
    For more general formulations, which are usually nonconvex, 
    we implement the successive convex approximation method proposed by Feng & Palomar (2015).

### Indicators

1. [TA-Lib](https://github.com/TA-Lib/ta-lib)
    is an open-source technical analysis library for financial applications. 
    It provides a wide range of technical indicators and functions for analyzing financial market data.

2. [indicator](https://github.com/cinar/indicator)
    is a Golang module providing various stock technical analysis indicators for trading.

3. [stock-indicators-python](https://github.com/facioquo/stock-indicators-python)
    is a PyPI library package that produces financial market technical indicators. 
    Send in historical price quotes and get back desired indicators 
    such as moving averages, Relative Strength Index, Stochastic Oscillator, Parabolic SAR, etc. Nothing more.
    [stock-indicators-python](https://github.com/facioquo/stock-indicators-python)
    is based on
    [Stock.Indicators](https://github.com/DaveSkender/Stock.Indicators)
    which is implemented in C#.

4. [Tulip Indicators](https://tulipindicators.org/)
    is a library of functions for technical analysis of financial time series data. 
    It is written in ANSI C for speed and portability. 
    Bindings are available for many other programming languages too.

5. [trade_aggregation-rs](https://github.com/MathisWellmann/trade_aggregation-rs)
    is a high performance, modular and flexible trade aggregation crate, producing Candle data, 
    suitable for low-latency applications and incremental updates. 
    It allows the user to choose the rule dictating how a new candle is created through the AggregationRule trait, e.g: Time, Volume based or some other information driven rule. 
    It also allows the user to choose which type of candle will be created from the aggregation process through the ModularCandle trait. 
    Combined with the Candle macro, it enables the user to flexibly create any type of Candle as long as each component implements the CandleComponent trait. 
    The aggregation process is also generic over the type of input trade data as long as it implements the TakerTrade trait, allowing for greater flexibility for downstream projects.

6. [sliding_features-rs](https://github.com/MathisWellmann/sliding_features-rs)
    provides modular, chainable sliding windows with various signal processing functions and technical indicators.

### Calendar

1. [python-bizdays] (https://github.com/wilsonfreitas/python-bizdays)
    offers business days calculations and utilities.

### Backtesting 

1. [bt](https://github.com/pmorissette/bt)
    is a flexible backtesting framework 
    for Python used to test quantitative trading strategies. 
    Backtesting is the process of testing a strategy over a given data set. 
    This framework allows you to easily create strategies that mix and match different Algos. 
    It aims to foster the creation of easily testable, 
    re-usable and flexible blocks of strategy logic 
    to facilitate the rapid development of complex trading strategies.

2. [vectorbt](https://github.com/polakowo/vectorbt)
    is a powerful Python library that enables easy backtesting 
    of trading strategies, financial data analysis, and visualization. 
    It provides a fast and efficient engine for quantitative finance research and algorithmic trading.

3. [qstrader](https://github.com/mhallsmoore/qstrader)
    is a free Python-based open-source modular schedule-driven backtesting framework 
    for long-short equities and ETF based systematic trading strategies.

### Deep Learning

1. [FinRL](https://github.com/AI4Finance-Foundation/FinRL)
    is an open-source framework for financial reinforcement learning. 
    It aims to revolutionize FinTech by providing a comprehensive ecosystem 
    for developing and deploying reinforcement learning-based trading strategies.

## Good Platfroms

[API Algo Trading Landscape](https://alpaca.markets/learn/algo-trading-landscape/)
has a good summary.

Charles Schwab supports algo trading via the thinkorswim® platform (thinkScript).
For more details,
please refer to
[Coding for Traders: Building Your Own Indicator](https://www.schwab.com/learn/story/coding-traders-building-your-own-indicator)
.
Charles Schwab is currently developing Trade APIs 
(both for commercial and individual)
.

[Alpaca](https://alpaca.markets/)

[9 Great Tools for Algo Trading](https://medium.com/hackernoon/9-great-tools-for-algo-trading-e0938a6856cd)
has a good summary 

In terms of cost to get started,
[Alpaca](https://alpaca.markets/) < [QuantConnect](https://www.quantconnect.com/pricing) < [QuantRocket](https://www.quantrocket.com/pricing/)
< [IteractiveBrokers](https://www.interactivebrokers.com/en/home.php)
.

## Open Source Trading Platforms/Projects

[MIT Open Course Ware - Trading](https://ocw.mit.edu/search/ocwsearch.htm?q=trading)

quantos, kungfu, vnpy, RQAlpha2

https://zhuanlan.zhihu.com/p/34822731

[Quantopian](https://github.com/quantopian)

[Quantitative Economics](https://python.quantecon.org/)

## Data Source

### [polygon.io](https://polygon.io/pricing)
[polygon.io](https://polygon.io/pricing)
is great data source with free plans available.

## Taxes

### Short-term taxes

### Wash Sale

Please refer to 
[Tips on Wash Sale]( https://www.legendu.net/misc/blog/tips-on-wash-sale )  
for detailed discussions.

## Order Types

- [Trailing Stop Orders](https://www.schwab.com/learn/story/trailing-stop-orders-mastering-order-types)

## Misc

http://www.zhihu.com/question/28557233?from=profile_question_card

http://myquant.cn/

http://www.vnpy.org/quantlib-tutorial.html

http://www.vnpy.org/talib-tutorial.html

http://www.vnpy.org/basic-tutorial-4.html

http://www.zhihu.com/question/33555640/answer/56820093

https://www.zhihu.com/question/25074959/answer/31184123?from=profile_answer_card

https://www.zhihu.com/question/21789812/answer/22369809

https://zhuanlan.zhihu.com/p/20505282?refer=edwardfuna

https://zhuanlan.zhihu.com/p/20502027?refer=edwardfuna

https://www.zhihu.com/question/34868706/answer/106024559

https://www.zhihu.com/question/36532600/answer/68127964?from=profile_answer_card

https://www.zhihu.com/question/31817168/answer/53462153

[Tow the Iceburg](https://www.zhihu.com/question/23667442/answer/28965906)

Prediction of Hidden Liquidity in the Limit Order Book of GLOBEX Futures

Mclean, R. David and Jeffrey Pontiff, 2016, Does Academic Research Destroy Stock Return Predictability, The Journal of Finance 71(1), 5-32.

## References

- [Investment](https://misc.legendu.net/blog/investment-tips/)

- [awesome-quant](https://github.com/wilsonfreitas/awesome-quant)

- [The first-timer’s guide to buying stocks](https://www.nerdwallet.com/m/investing/how-to-buy-stocks-cs?bucket_id=Without+Chase&gad_source=1&gclid=CjwKCAiAgeeqBhBAEiwAoDDhn-ZlWJMKfNxBXeHm5f7iTKol0KmclBRNnVBNIbOUYG_KFIesxDvyVhoCNegQAvD_BwE&gclsrc=aw.ds&mktg_body=2989&mktg_hline=19335&mktg_place=aud-2205081372215%3Akwd-21866581&model_execution_id=D27E7BC4-58F9-46C0-B087-21293245805C&nw_campaign_id=154950223590786600&utm_campaign=in_mktg_paid_072023_stocks_upper-funnel_broad_desktop&utm_content=ta&utm_medium=cpc&utm_source=goog&utm_term=learn+about+stocks)

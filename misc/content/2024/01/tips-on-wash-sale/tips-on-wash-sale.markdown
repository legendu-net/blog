Status: published
Date: 2024-01-15 01:11:58
Modified: 2024-01-15 10:27:51
Author: Benjamin Du
Slug: tips-on-wash-sale
Title: Tips on Wash Sale
Category: Investment
Tags: Investment, wash sale, IRS, tax, quant, trading

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Some Tips on Tax Consequences of Wash Sales

1. Make sure the last trade is a "buy" 
    and avoid buying the same stock/security in Dec and Jan (next year).
    Assuming the trading market is open on Dec 31,
    you can then sell the last buy (more than 30 days agao).
    Since there is no purchase of the same stock/security in Jan,
    i.e., more than 30 days following the sale in Dec,
    the sale in Dec is not considered a wash sale if there's a loss. 
    This means that you can deduct your capital loss for tax purposes.
    To make tax calculations easier,
    try to buy and sell the same quantity of the same stock/security.

2. Try to make each sale profitable by carefully choosing which lots of shares to sell.
    This is (partially) possible with some trading APIs 
    (e.g., IB trading APIs allowing specifying FIFO, FILO strategies)
    but is not universally implemented
    (e.g., Alpaca API does not support it yet)
    .

## References

- [WASH SALES FOR TRADERS - A GUIDE TO THE IRS WASH SALE RULE AND HOW TRADERS CONTROL THE EFFECTS](https://tradelog.com/education/wash-sales-for-traders/)

- [Wash Rule Impact on Algo Trading](https://www.reddit.com/r/algotrading/comments/mhk2d6/wash_rule_impact_on_algo_trading/)

- [Trader Status - Is it wise to trade in one’s own name and claim trader status?](https://andersonadvisors.com/trader-taxation/)

- [Selling specific lots of shares](https://forum.alpaca.markets/t/selling-specific-lots-of-shares/956)

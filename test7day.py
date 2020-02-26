from datetime import datetime
import backtrader as bt
import sys

stocksymbol = sys.argv[1]
print(stocksymbol)

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()
#cerebro.addstrategy(SmaCross)

data0 = bt.feeds.YahooFinanceData(dataname=stocksymbol, fromdate=datetime(2020, 2, 19),
                                  todate=datetime(2020, 2, 26))
cerebro.adddata(data0)

cerebro.run()

cerebro.plot(None,1,True,None,None,16,9,300,True,None,'/var/www/html/chart.png')

#figs[0].savefig('plot.png')

#print(figs[0])

#figs.plot_components(fig).savefig('info.png',300)

#figs.savefig(path,300)


#print(figs)


package stocks

// Author:	DragonChen https://github.com/dragonchen-tw/
// Title:	portfolio package
// Date:	2022/08/30

type Portfolio []Money

func (p Portfolio) Add(money Money) Portfolio {
	p = append(p, money)
	return p
}

func (p Portfolio) Evaluate(currency string) Money {
	total := 0.0
	for _, m := range p {
		total += convert(m, currency)
	}
	return Money{amount: total, currency: currency}
}

func convert(m Money, currency string) float64 {
	if m.currency == currency {
		return m.amount
	}

	exchangeRates := map[string]float64{
		"EUR->USD": 1.2,
		"USD->KRW": 1100,
	}

	key := m.currency + "->" + currency
	return m.amount * exchangeRates[key]
}

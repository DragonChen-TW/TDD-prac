package stocks

import "errors"

// Author:	DragonChen https://github.com/dragonchen-tw/
// Title:	portfolio package
// Date:	2022/08/30

type Portfolio []Money

func (p Portfolio) Add(money Money) Portfolio {
	p = append(p, money)
	return p
}

func (p Portfolio) Evaluate(bank Bank, currency string) (*Money, error) {
	total := 0.0
	failedConversions := make([]string, 0)
	for _, m := range p {
		if converterMoney, ok := bank.Convert(m, currency); ok != nil {
			failedConversions = append(failedConversions, m.currency+"->"+currency)
		} else {
			total += converterMoney.amount
		}
	}

	if len(failedConversions) != 0 {
		failures := "["
		for _, f := range failedConversions {
			failures += f + ","
		}
		failures += "]"

		return nil, errors.New("Missing exchange rate(s):" + failures)
	}

	var result Money
	result = NewMoney(total, currency)
	return &result, nil
}

func convert(m Money, currency string) (float64, bool) {
	exchangeRates := map[string]float64{
		"EUR->USD": 1.2,
		"USD->KRW": 1100,
	}

	if m.currency == currency {
		return m.amount, true
	}
	key := m.currency + "->" + currency
	rate, ok := exchangeRates[key]
	return m.amount * rate, ok
}

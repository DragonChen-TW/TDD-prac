package stocks

import "errors"

// Author:	DragonChen https://github.com/dragonchen-tw/
// Title:	bank package
// Date:	2022/09/01

type Bank struct {
	exchangeRates map[string]float64
}

func NewBank() Bank {
	return Bank{exchangeRates: make(map[string]float64)}
}

func (bank Bank) AddExchangeRate(fromCurrency, toCurrency string, rate float64) {
	key := fromCurrency + "->" + toCurrency
	bank.exchangeRates[key] = rate
}

func (bank Bank) Convert(money Money, currencyTo string) (*Money, error) {
	if money.currency == currencyTo {
		return &money, nil
	}

	key := money.currency + "->" + currencyTo
	rate, ok := bank.exchangeRates[key]

	if !ok {
		return nil, errors.New(key)
	}

	return &Money{money.amount * rate, currencyTo}, nil
}

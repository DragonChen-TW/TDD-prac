package main

import (
	"testing"
)

// Author:	DragonChen https://github.com/dragonchen-tw/
// Title:	ch1 Money Test
// Date:	2022/08/30

func assertEqual(t *testing.T, expected, actual Money) {
	if expected != actual {
		t.Errorf("Expected [%+v] Got [%+v]", expected, actual)
	}
}

func TestMultiplicationInDollars(t *testing.T) {
	fiver := Money{amount: 5, currency: "USD"}
	actualResult := fiver.Times(2)
	expectedResult := Money{amount: 10, currency: "USD"}
	assertEqual(t, expectedResult, actualResult)
}

func TestMultiplicationInEuros(t *testing.T) {
	tenEuros := Money{amount: 10, currency: "EUR"}
	actualResult := tenEuros.Times(2)
	expectedResult := Money{amount: 20, currency: "EUR"}
	assertEqual(t, expectedResult, actualResult)
}

func TestDivision(t *testing.T) {
	originalMoney := Money{amount: 4002, currency: "KRW"}
	actualMoneyAfterDivision := originalMoney.Divide(4)
	expectedMoneyAfterDivision := Money{amount: 1000.5, currency: "KRW"}
	assertEqual(t, expectedMoneyAfterDivision, actualMoneyAfterDivision)
}

func TestAddition(t *testing.T) {
	var profolio Profolio
	var profolioInDollars Money

	fiveDollars := Money{amount: 5, currency: "USD"}
	tenDollars := Money{amount: 10, currency: "USD"}
	fifteenDollars := Money{amount: 15, currency: "USD"}

	profolio = profolio.Add(fiveDollars)
	profolio = profolio.Add(tenDollars)
	profolioInDollars = profolio.Evaluate("USD")

	assertEqual(t, fifteenDollars, profolioInDollars)
}

type Money struct {
	amount   float64
	currency string
}

func (m Money) Times(multiplier int) Money {
	return Money{amount: m.amount * float64(multiplier), currency: m.currency}
}

func (m Money) Divide(divisor int) Money {
	return Money{amount: m.amount / float64(divisor), currency: m.currency}
}

type Profolio []Money

func (p Profolio) Add(money Money) Profolio {
	p = append(p, money)
	return p
}

func (p Profolio) Evaluate(currency string) Money {
	total := 0.0
	for _, m := range p {
		total += m.amount
	}
	return Money{amount: total, currency: currency}
}

package main

import (
	s "tdd/stocks"
	"testing"
)

// Author:	DragonChen https://github.com/dragonchen-tw/
// Title:	ch1 Money Test
// Date:	2022/08/30

func assertEqual(t *testing.T, expected, actual s.Money) {
	if expected != actual {
		t.Errorf("Expected [%+v] Got [%+v]", expected, actual)
	}
}

func TestMultiplication(t *testing.T) {
	tenEuros := s.NewMoney(10, "EUR")
	actualResult := tenEuros.Times(2)
	expectedResult := s.NewMoney(20, "EUR")
	assertEqual(t, expectedResult, actualResult)
}

func TestDivision(t *testing.T) {
	originalMoney := s.NewMoney(4002, "KRW")
	actualMoneyAfterDivision := originalMoney.Divide(4)
	expectedMoneyAfterDivision := s.NewMoney(1000.5, "KRW")
	assertEqual(t, expectedMoneyAfterDivision, actualMoneyAfterDivision)
}

func TestAddition(t *testing.T) {
	var profolio s.Profolio
	var profolioInDollars s.Money

	fiveDollars := s.NewMoney(5, "USD")
	tenDollars := s.NewMoney(10, "USD")
	fifteenDollars := s.NewMoney(15, "USD")

	profolio = profolio.Add(fiveDollars)
	profolio = profolio.Add(tenDollars)
	profolioInDollars = profolio.Evaluate("USD")

	assertEqual(t, fifteenDollars, profolioInDollars)
}

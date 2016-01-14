#!/usr/bin/env python
# encoding: utf-8

class Solution {
public:
    string intToRoman(int num) {
        string thousand[4] = {"", "M", "MM","MMM"};
        string hundred[11] = {"", "C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        string ten[11] = {"", "X", "XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        string one[11] = {"", "I","II","III","IV","V","VI","VII","VIII","IX"};
        string result = "";
        string* trans[4] = {one, ten, hundred, thousand};
        int index = 0;
        while (num > 0) {
            result = trans[index][num % 10] + result;
            num = num / 10;
            index++;
        }
        return result;
    }
};
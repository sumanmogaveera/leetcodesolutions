class Solution {
    public boolean halvesAreAlike(String s) {
        int a = 0, b = 0;
        s = s.toLowerCase();
        for (int i = 0; i < s.length() / 2; i++) {
            if ("aeiou".contains(s.charAt(i) + "")) a++;
            if ("aeiou".contains(s.charAt(i + s.length()/2) + "")) b++;
        }
        return a == b;
    }
}
class Solution {
public:
    int mirrorReflection(int p, int q) {
        int f = gcd(p, q);
        int m = p*q/f;
        if ((m/q) % 2 == 0)
            return 2;
        if ((m / p) % 2 == 1)
            return 1;
        return 0;
    }
    int gcd(int m, int n) {
        if (n == 0) return m;
        return gcd(n, m%n);
    }
};
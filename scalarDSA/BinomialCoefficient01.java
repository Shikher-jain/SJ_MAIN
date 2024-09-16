// package SJ_MAIN.scalarDSA;

class BinomialCoefficient01 {

    public static long binomialCoefficient(int n, int k) {
        if (k > n - k) {
            k = n - k;  // symmetry
        }
        
        long result = 1;
        for (int i = 0; i < k; i++) {
            result *= (n - i);
            result /= (i + 1);
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 5, k = 2;
        System.out.println("Binomial Coefficient C(" + n + ", " + k + ") = " + binomialCoefficient(n, k));
    }
}

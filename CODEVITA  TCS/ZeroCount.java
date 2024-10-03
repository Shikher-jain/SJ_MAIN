import java.util.Scanner;

public class ZeroCount {
    public static int longestContiguousZeros(int B, int K) {
        int Z = B - K;  // Total number of zeros
        if (K == 0) {  // All zeros
            return Z;
        }
        if (K >= B) {  // All ones
            return 0;
        }
        
        // Calculate how to distribute zeros
        int base = Z / (K + 1);
        int extra = Z % (K + 1);
        
        // If there are extra zeros,
        //  the maximum length of zeros will be base + 1
        if (extra > 0) {
            return base + 1;
        } else {
            return base;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int B = scanner.nextInt();
        int K = scanner.nextInt();
        
        // int B = 3;   
        // int K = 1;   
        
        int result = longestContiguousZeros(B, K);
        System.out.println(result);
        
        scanner.close();
    }
}


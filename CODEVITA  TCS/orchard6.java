import java.util.Scanner;

public class orchard6 {
    public static int countValidCombination(String row) {
        int mCount = 0; // Count of 'M'
        int lCount = 0; // Count of 'L'
        
        // Count the occurrences of 'M' and 'L'
        for (char c : row.toCharArray()) {
            if (c == 'M') {
                mCount++;
            } else if (c == 'L') {
                lCount++;
            }
        }
        
        // Calculate valid combinations
        if (mCount >= 1 && lCount >= 1) {
            return mCount * lCount * (mCount + lCount - 2);
        }
        return 0; // No valid combinations
    }

    public static String winner(String row1, String row2) {
        // Validate input strings
        if (!row1.matches("[ML]*") || !row2.matches("[ML]*")) {
            return "Invalid input";
        }
        
        int count1 = countValidCombination(row1);
        int count2 = countValidCombination(row2);
        
        // Determine the winner
        if (count1 > count2) {
            return "Ashok";
        } else if (count2 > count1) {
            return "Anand";
        } else {
            return "Draw";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String row1 = scanner.nextLine();
        String row2 = scanner.nextLine();
        String result = winner(row1, row2);
        System.out.println(result);
        scanner.close();
    }
}


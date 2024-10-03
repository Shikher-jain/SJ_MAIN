import java.util.Scanner;

class Solution {
    public static int countValidCombination(String row) {
        int m = 0; // Count of 'M'
        int l = 0; // Count of 'L'
        
        // Count 'M's and 'L's
        for (char c : row.toCharArray()) {
            if (c == 'M') {
                m++;
            } else if (c == 'L') {
                l++;
            }
        }
        
        // Calculate valid combinations
        if (m >= 1 && l >= 1) {
            return m * l * (m + l - 2);
        }
        return 0; // If no valid combinations can be formed
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
}

public class orchard2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String row1 = scanner.nextLine();
        String row2 = scanner.nextLine();
        Solution obj = new Solution();
      
        String result = Solution.winner(row1, row2);
        System.out.println(result);
        scanner.close();
    }
}

import java.util.Scanner;

public class orchard5 {
    public static int countValidCombinations(String row) {
        int count = 0;
        int n = row.length();
        
        // Check for combinations of three trees
        for (int i = 0; i < n - 2; i++) {
            if (row.charAt(i) != row.charAt(i + 1) && row.charAt(i) != row.charAt(i + 2) && row.charAt(i + 1) != row.charAt(i + 2)) {
                count++;
            }
        }
        
        return count;
    }

    public static String winner(String row1, String row2) {
        // Validate input strings
        if (!row1.matches("[ML]*") || !row2.matches("[ML]*")) {
            return "Invalid input";
        }

        // Count valid combinations
        int count1 = countValidCombinations(row1);
        int count2 = countValidCombinations(row2);
        
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

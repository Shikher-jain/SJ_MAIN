import java.util.*;

public class LegalSubset {

    public static List<String> findSubsets(int N, long R, String strings) {
        List<String> subsets = new ArrayList<>();
        subsets.add(""); // Rank 1: Empty set

        // Split input strings into a list
        List<String> stringsList = Arrays.asList(strings.split(","));
        
        // Add individual strings as subsets with ranks 2 to N + 1
        subsets.addAll(stringsList);

        // Generate subsets with combinations of strings
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                String subset = stringsList.get(i) + "," + stringsList.get(j);
                
                // Check if this subset is legal
                boolean legal = true;
                for (int k = j + 1; k < N; ++k) {
                    int pos1 = subset.indexOf(stringsList.get(k));
                    int pos2 = subset.indexOf(",", pos1);
                    
                    // Adjust legality based on your specific requirements
                    if (pos1 != -1 && pos2 == -1) {
                        legal = false;
                        break;
                    }
                }
                
                // If legal, add it to the subsets
                if (legal) {
                    subsets.add(subset);
                }
            }
        }

        // Sort subsets based on size and order of appearance
        subsets.sort(Comparator.comparingInt(String::length).thenComparing(subset -> {
            List<String> items = Arrays.asList(subset.split(","));
            return stringsList.indexOf(items.get(0));
        }));

        // Check if R is within valid bounds
        List<String> result = new ArrayList<>();
        if (R > 0 && R <= subsets.size()) {
            result.add(subsets.get((int) R - 1));
        } else {
            result.add("Invalid rank"); // Handle invalid R
        }
        return result;
    }

    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        long R = scanner.nextLong();
        scanner.nextLine(); // Consume the newline character
        String strings = scanner.nextLine();

        // Find the R-th subset
        List<String> result = findSubsets(N, R, strings);
        
        // Output the R-th subset
        System.out.println(result.get(0));
    }
}

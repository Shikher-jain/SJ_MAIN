import java.util.Scanner;

public class BestBubble {
    public static int totalDist(String name, String GoodStr) {
        int Distance = 0;
        char PrevGood = GoodStr.charAt(0);

        for (char charName : name.toCharArray()) {
            if (GoodStr.indexOf(charName) != -1) {
                PrevGood = charName;
                continue;
            }

            int MDistance = Integer.MAX_VALUE;
            Character Best = null;

            for (char Good : GoodStr.toCharArray()) {
                int distance = Math.abs(charName - Good);

                if (distance < MDistance) {
                    MDistance = distance;
                    Best = Good;
                } else if (distance == MDistance) {
                    if (Math.abs(PrevGood - Good) < Math.abs(PrevGood - Best)) {
                        Best = Good;
                    }
                }
            }
            Distance += MDistance;
            PrevGood = Best;
        }
        return Distance;
    }

    public static int bubble(int n, int[] arr, boolean order) {
        int swap = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if ((!order && arr[j] < arr[j + 1]) || (order && arr[j] > arr[j + 1])) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                    swap++;
                }
            }
        }
        return swap;
    }

    public static int Mswap(int n, int[] arr) {
        int ascendingOrder = bubble(n, arr.clone(), true);
        int descendingOrder = bubble(n, arr.clone(), false);
        return Math.min(ascendingOrder, descendingOrder);
    }
  
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            String name = scanner.nextLine();
            String GoodStr = scanner.nextLine();
            int Distance = totalDist(name, GoodStr);
            System.out.println(Distance);
        }
    }
}
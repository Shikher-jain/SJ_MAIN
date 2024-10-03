import java.util.Scanner;

public class Goodstring {
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

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        String GoodStr = scanner.nextLine();
        int Distance = totalDist(name, GoodStr);
        System.out.println(Distance);
        scanner.close();
    }
}


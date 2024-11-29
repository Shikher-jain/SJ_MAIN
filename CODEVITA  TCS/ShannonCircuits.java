// import java.util.*;

// class ShanonCircuit {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner();

//         int n = Integer.parseInt(sc.nextLine());
//         Map<String,String[]> gates =new Hashmap <>();

//         for (int i=0;i<n;i++){
//             String[] parts = sc.nextLine().split("=");
//             String gateName = parts[0].trim();
//             String[] gateDefinition =parts[1].trim().split( "[(), ]");
//             gates.put(gateName,gateDefinition);
//         }
         

//         int t = Integer.parseInt(sc.nextLine());
//         Map<String,int[]> values =new Hashmap <>();
//         while (true){
//             String line = sc.nextLine();
//             if (line.matches("[a-zA-Z]")){
//                 String targetGate = line.trim();
//                 simulateCircuit(gates,values,targetGate,t);
//                 break;
//             }
        
//             String[] parts =line.split(" ");
//             String inputVar = parts[0]
//             int[] timings=Arrays.stream(parts,1,parts.length)
//                                 .mapToInt(Integer::parseInt)
//                                 .toArray();
//             values.put(inputVar,timings);
        
//         }
//     }

//     private static void simulateCircuit(Map<String, String[]> gates,Map<String,int[]> values,String targetGate,int t){
//         Map<String, int[]> outputs = new HashMap<>();
//         for(String gate : gates.keySet()){
//             outputs.put(gate, new int[t]);
//         }



//     }
// }


import java.util.*;

public class ShannonCircuits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Number of gates
        int n = Integer.parseInt(sc.nextLine());
        Map<String, String[]> gates = new HashMap<>(); // Gate definitions

        // Parse gate definitions
        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().split("=");
            String gateName = parts[0].trim(); // Gate output
            String[] gateDefinition = parts[1].trim().split("[(), ]+");
            gates.put(gateName, gateDefinition);
        }

        // Length of cycles
        int t = Integer.parseInt(sc.nextLine());
        // Parse input variables
        Map<String, int[]> values = new HashMap<>();
        while (true) {
            String line = sc.nextLine();
            if (line.matches("[a-zA-Z]+")) {
                // The last line specifies the target gate
                String targetGate = line.trim();
                simulateCircuit(gates, values, targetGate, t);
                break;
            }
            String[] parts = line.split(" ");
            String inputVar = parts[0];
            int[] timings = Arrays.stream(parts, 1, parts.length)
                    .mapToInt(Integer::parseInt)
                    .toArray();
            values.put(inputVar, timings);
        }
        sc.close();
    }

    private static void simulateCircuit(Map<String, String[]> gates, Map<String, int[]> values, String targetGate, int t) {
        Map<String, int[]> outputs = new HashMap<>();
        // Initialize outputs for all gates.
        for (String gate : gates.keySet()) {
            outputs.put(gate, new int[t]);
        }

        // Simulate each cycle
        for (int cycle = 1; cycle < t; cycle++) {
            for (String gate : gates.keySet()) {
                String[] definition = gates.get(gate);
                String operation = definition[0];
                String input1 = definition[1];
                String input2 = definition[2];

                int value1 = getValue(input1, outputs, values, cycle - 1);
                int value2 = getValue(input2, outputs, values, cycle - 1);

                // Compute the output based on the operation
                int result = computeGate(operation, value1, value2);
                outputs.get(gate)[cycle] = result;
            }
        }

        // Print the output for the target gate
        int[] targetOutput = outputs.get(targetGate);
        for (int i = 0; i < t; i++) {
            System.out.print(targetOutput[i] + (i == t - 1 ? "\n" : " "));
        }
    }

    private static int getValue(String var, Map<String, int[]> outputs, Map<String, int[]> values, int cycle) {
        if (values.containsKey(var)) {
            return values.get(var)[cycle];
        } else {
            return outputs.get(var)[cycle];
        }
    }

    // Updated to use traditional switch statement
    private static int computeGate(String operation, int value1, int value2) {
        int result = 0;
        switch (operation) {
            case "AND":
                result = value1 & value2;
                break;
            case "OR":
                result = value1 | value2;
                break;
            case "NAND":
                result = ~(value1 & value2) & 1; // Keep binary representation
                break;
            case "NOR":
                result = ~(value1 | value2) & 1; // Keep binary representation
                break;
            case "XOR":
                result = value1 ^ value2;
                break;
            default:
                result = 0; // Invalid operation
                break;
        }
        return result;
    }
}
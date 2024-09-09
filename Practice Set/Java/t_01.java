import java.util.*;
class t_01{
    public static void main(String[] args) {
        System.out.println("hi");

        List<Integer> l1=new ArrayList<>();

        l1.add(4);
        l1.add(3);
        l1.add(2);
        l1.add(1);
        l1.add(0);
        
        List<Integer> l2=new LinkedList<>();
        l2.add(1);
        l2.add(2);
        l2.add(3);
        l2.add(4);
        l2.add(5);
        
        System.out.println(l2);
        System.out.println(l1);
     
        Iterator <Integer> it1 =l1.listIterator();
        while(it1.hasNext())
        System.out.println(it1.next());

        Iterator <Integer> it2 =l1.listIterator();
        while(it2.hasNext())
        System.out.println(it2.next());
        }
    }
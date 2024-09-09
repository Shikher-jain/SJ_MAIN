class A {
    // A() {
    //     System.out.println("without parameters");
    // }
    // A(int a) {
    //     System.out.println("with int parameters " + a);
    // }
    // A(double a) {
    //     System.out.println("with double parameters " + a);
    // }
    void A1(String s) {
        System.out.println(s);
    }
}

class B extends A {
    B() {
        // System.out.println("Child");
    }
}

class C extends B{
    C(){
        // System.out.println("Grandchild");
    }
}
public class Main01 {
    public static void main(String[] args) {
        // System.out.println("Hello");
        // new A();
        // new A(12);
        // new A(34.7);
        A a = new A();
        a.A1("accecsed by Parent");

        B b = new B();
        b.A1("accecsed by Child");
        
        C c = new C();
        c.A1("accecsed by GrandChild");
        
        // new A().A1("accecsed by Parent");   
    }
}

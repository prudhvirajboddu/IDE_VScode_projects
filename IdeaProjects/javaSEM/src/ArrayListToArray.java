import java.util.*;
public class ArrayListToArray {
    public static void main(String args[])

    {
        ArrayList<String> a =new ArrayList<String>();
        a.add("Ml");
        a.add("AI");
        a.add("Will");
        a.add("Change");
        a.add("The");
        a.add("World");
        a.add("one");
        a.add("day");
        String st[]=a.toArray(new String[a.size()]);
        System.out.println("Elements are");
        for (String k:st)
            System.out.println(k);

    }

}

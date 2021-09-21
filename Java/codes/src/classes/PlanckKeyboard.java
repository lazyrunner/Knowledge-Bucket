package classes;

public class PlanckKeyboard implements IKeyboard {

    @Override
    public int getPrice() {
        return 50000;
    }

    @Override
    public String getType() {
        return "Planck";
    }
}

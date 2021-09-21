package classes;

public class MoonLanderKeyboard implements IKeyboard {
    @Override
    public int getPrice() {
        return 300000;
    }

    @Override
    public String getType() {
        return "Moonlander";
    }
}

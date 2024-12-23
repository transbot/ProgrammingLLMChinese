namespace Prenoto.BookingLogic
{
    public class RoomType
    {
        public static RoomType Single() 
        {
            return new RoomType(
                "单人间",
                "对单人间的简单描述。",
                Price.Dollar(200));
        }
        public static RoomType Double()
        {
            return new RoomType(
                "双人间",
                "对双人章的简单描述。",
                Price.Dollar(300));
        }
        public RoomType(string name, string description, Price price)
        {
            Name = name;
            Description = description;
            PricePerNight = price;
        }
        public string Name { get; set; }
        public string Description { get; set; }
        public Price PricePerNight { get; set; }
    }

    public class Price 
    {
        public Price(string currency, float amount)
        {
            Currency = currency;
            Amount = amount;
        }
        public static Price Dollar(float amount)
        {
            return new Price("USD", amount);
        }
        public string Currency { get; set; }
        public float Amount { get; set; }
    }
}

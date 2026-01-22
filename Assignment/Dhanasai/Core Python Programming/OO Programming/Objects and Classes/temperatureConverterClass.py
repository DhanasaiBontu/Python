class Temperature:
    def to_celcius(self,f):
        return (f - 32) * 5/9
    def to_fahrenheit(self,c):
        return (c * 9/5) + 32
t = Temperature()
print(t.to_fahrenheit(0))
def two_numbers():
    total = 0
    for 
























    

 public int multiplyfeature ( int digit, int multiply ) {
    int total = 0;
    for ( int i = 0; i <= multiply; i++ ) {
      total *= digit; 
    }
    return total;
    
    
 public void testMultiplyFeature() {
    SimpleCalculator myCalculator = new SimpleCalculator();
    int multiply = myCalculator.multiplyfeature(2, 5);
    assertEquals(10, multiply);
  }

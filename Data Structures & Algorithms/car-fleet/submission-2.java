class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int fleets = 0;
        List<Integer> ind = IntStream.range(0, position.length)
        .boxed()
        .sorted((a, b) -> Integer.compare(position[b], position[a]))
        .collect(Collectors.toList());

        double prevTime = 0;
        for (int i = 0; i < position.length; i++) {
            double newTime = (double) (target - position[ind.get(i)]) / speed[ind.get(i)];
            if (newTime > prevTime) {
                fleets += 1;
                prevTime = newTime;
            }
        }
        return fleets;
    }
}

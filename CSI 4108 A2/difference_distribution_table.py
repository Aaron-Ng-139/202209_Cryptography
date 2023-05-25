# Difference Distribution Table

# My 4-bit s-box
inputX = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
outputY = [10,9,8,3,2,5,13,6,1,4,11,15,14,12,0,7] # Created by myself
# outputY = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7] # Textbook Example

# Difference Distribution Table
diffDistribution = []

# For all input differences 0-15
for xShift in range(16):
    yShift = []
    # Iterate through all values x from 0-15
    for x in range(16):
        # Calculate output differences after being put through s-box
        yShift.append(outputY[x] ^ outputY[x ^ xShift])
    
    # Count number of occurances of each value
    yShiftCount = []
    for i in range(16):
        yShiftCount.append(yShift.count(i))
    
    # Save to difference distribution table
    diffDistribution.append(yShiftCount)
    

for i in range(16):
    print(diffDistribution[i])
def percentage(room,size):   #calculates the percentage of the room that is visible

    viewedarea = room!= 0  # Here a Boolean matrix is returned where "True" means visible, wall, table or guard
    viewedblocks = sum(sum(viewedarea))  # Sums the amount of visible 'blocks'
    perc = viewedblocks / (size[0] * size[1]) * 100  # calculates % of viewed blocks
    return perc
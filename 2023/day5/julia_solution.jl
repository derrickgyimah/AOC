seed = [247767461, 64738286, 66221787, 103070898, 261552692, 257826205, 65672948, 300163578, 82800966, 229295075]
rang = [1187290020, 40283135, 2044483296, 1777809491, 108732160, 3810626561, 3045614911, 744199732, 3438684365, 2808575117]

new_seed_values = []

for (s, r) in zip(seed, rang)
    println(r)
    append!(new_seed_values, s)
    println(r)
    append!(new_seed_values, s .+ 1:s .+ r .- 1)
    println(r)
end

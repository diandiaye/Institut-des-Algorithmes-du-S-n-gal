
# Institut des Algorithmes du Sénégal

 ```ruby
 function Pₓ(a,b,c)
    println("*"^100)
    if a==0
        println("L'équation n'est pas du second degré")
    else
        b²=b*b
        Δ=b²-4*a*c
        if Δ<0
            println("L'équation\n $(string(a,base=2,pad=1))x²+$(string(b,base=2,pad=1))x+$c
            n'admet pas de solutions réelles\n")
        elseif Δ==0
            x₀=-b/2*a
            println("L'équation\n $(string(a,base=2,pad=1))x²+$(string(b,base=2,pad=1))x+$c
            admet une solution double x₀=-b/2×a=$x₀\n")
        elseif Δ>0
            x₁=(-b-√Δ)/2*a
            x₂=(-b+√Δ)/2*a
            println("L'équation\n $(string(a,base=2,pad=1))x²+$(string(b,base=2,pad=1))x+$c
            admet deux solutions distinctes
            ⟨x₁,x₂⟩ = ⟨ (-b-√Δ)/2×a , (-b-√Δ)/2×a ⟩ = ⟨$x₁,$x₂⟩\n")
        end
    end
    println("*"^100)
end
Pₓ(2,3,-2)
Pₓ(2,3,2)
Pₓ(1,2,1)
Pₓ(0,2,1)

#=********************************************************************************
*

  ```

import java.util.*

fun main() {
    val n = readLine()!!.toInt()
    var count = 0
    for( i in 1..n) {
        for(j in 1..n){
            if(i * j <= n -1){
                count += 1
            }else{
                break
            }
        }
    }
    println(count)
}
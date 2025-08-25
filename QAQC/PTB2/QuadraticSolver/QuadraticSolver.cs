using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuadraticSolver
{
    public class QuadraticSolver
    {
        public static string Solve(double a, double b, double c)
        {
            if (a == 0)
            {
                if (b == 0)
                {
                    return c == 0 ? "Vô số nghiệm" : "Vô nghiệm";
                }
                return $"Một nghiệm: x = {-c / b}";
            }

            double delta = b * b - 4 * a * c;
            if (delta < 0)
            {
                return "Vô nghiệm";
            }
            else if (delta == 0)
            {
                double x = -b / (2 * a);
                return $"Nghiệm kép: x = {x}";
            }
            else
            {
                double x1 = (-b + Math.Sqrt(delta)) / (2 * a);
                double x2 = (-b - Math.Sqrt(delta)) / (2 * a);
                return $"Hai nghiệm: x1 = {x1}, x2 = {x2}";
            }
        }
    }
}

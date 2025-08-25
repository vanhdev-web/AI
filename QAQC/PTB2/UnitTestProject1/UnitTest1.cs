using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using QuadraticSolver;

namespace QuadraticSolverTests
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void Test_VoSoNghiem()
        {
            string result = QuadraticSolver.QuadraticSolver.Solve(0, 0, 0);
            Assert.AreEqual("Vô số nghiệm", result);
        }

        [TestMethod]
        public void Test_VoNghiem_Bac1()
        {
            string result = QuadraticSolver.QuadraticSolver.Solve(0, 0, 5);
            Assert.AreEqual("Vô nghiệm", result);
        }

        [TestMethod]
        public void Test_PhuongTrinhBac1()
        {
            string result = QuadraticSolver.QuadraticSolver.Solve(0, 2, -4);
            Assert.AreEqual("Một nghiệm: x = 2", result);
        }

        [TestMethod]
        public void Test_NghiemKep()
        {
            string result = QuadraticSolver.QuadraticSolver.Solve(1, 2, 1);
            Assert.AreEqual("Nghiệm kép: x = -1", result);
        }

        [TestMethod]
        public void Test_HaiNghiem()
        {
            string result = QuadraticSolver.QuadraticSolver.Solve(1, -3, 2);
            Assert.AreEqual("Hai nghiệm: x1 = 2, x2 = 1", result);
        }

        [TestMethod]
        public void Test_VoNghiem_Bac2()
        {
            string result = QuadraticSolver.QuadraticSolver.Solve(1, 0, 1);
            Assert.AreEqual("Vô nghiệm", result);
        }
    }
}

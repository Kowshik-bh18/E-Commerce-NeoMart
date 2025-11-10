import React from "react";
import {
  Box,
  Flex,
  Button,
  Link as ChakraLink,
  useToast,
} from "@chakra-ui/react";
import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();
  const toast = useToast();
  const token = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    toast({
      title: "Success",
      description: "Logged out successfully",
      status: "success",
      duration: 3000,
      isClosable: true,
    });
    navigate("/login");
  };

  return (
    <Box bg="blue.500" px={4} py={4}>
      <Flex
        maxW="container.xl"
        mx="auto"
        align="center"
        justify="space-between"
      >
        <Flex>
          <ChakraLink as={Link} to="/" color="white" fontWeight="bold" mr={6}>
            NeoMart
          </ChakraLink>
          <ChakraLink as={Link} to="/cart" color="white" mr={6}>
            Cart
          </ChakraLink>
          {token && (
            <ChakraLink as={Link} to="/orders" color="white">
              Orders
            </ChakraLink>
          )}
        </Flex>

        <Flex>
          {token ? (
            <Button colorScheme="whiteAlpha" onClick={handleLogout}>
              Logout
            </Button>
          ) : (
            <>
              <Button as={Link} to="/login" colorScheme="whiteAlpha" mr={4}>
                Login
              </Button>
              <Button as={Link} to="/register" colorScheme="whiteAlpha">
                Register
              </Button>
            </>
          )}
        </Flex>
      </Flex>
    </Box>
  );
}

export default Navbar;

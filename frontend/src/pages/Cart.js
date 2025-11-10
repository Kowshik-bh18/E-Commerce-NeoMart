import React, { useState, useEffect } from "react";
import {
  Box,
  Container,
  Heading,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Button,
  Text,
  useToast,
} from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import { getCart } from "../services/api";

function Cart() {
  const [cartItems, setCartItems] = useState([]);
  const [total, setTotal] = useState(0);
  const navigate = useNavigate();
  const toast = useToast();

  useEffect(() => {
    loadCart();
  }, []);

  const loadCart = async () => {
    try {
      const data = await getCart();
      setCartItems(data.results || []);
      calculateTotal(data.results);
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to load cart",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    }
  };

  const calculateTotal = (items) => {
    const sum = items.reduce((acc, item) => {
      return acc + item.product_details.price * item.quantity;
    }, 0);
    setTotal(sum);
  };

  const handleCheckout = () => {
    navigate("/checkout");
  };

  return (
    <Container maxW="container.xl" py={8}>
      <Heading mb={6}>Shopping Cart</Heading>

      {cartItems.length === 0 ? (
        <Text>Your cart is empty</Text>
      ) : (
        <>
          <Table variant="simple">
            <Thead>
              <Tr>
                <Th>Product</Th>
                <Th>Price</Th>
                <Th>Quantity</Th>
                <Th>Total</Th>
              </Tr>
            </Thead>
            <Tbody>
              {cartItems.map((item) => (
                <Tr key={item.id}>
                  <Td>{item.product_details.name}</Td>
                  <Td>${item.product_details.price}</Td>
                  <Td>{item.quantity}</Td>
                  <Td>${item.product_details.price * item.quantity}</Td>
                </Tr>
              ))}
            </Tbody>
          </Table>

          <Box mt={6} textAlign="right">
            <Text fontSize="xl" fontWeight="bold" mb={4}>
              Total: ${total}
            </Text>
            <Button colorScheme="blue" onClick={handleCheckout}>
              Proceed to Checkout
            </Button>
          </Box>
        </>
      )}
    </Container>
  );
}

export default Cart;

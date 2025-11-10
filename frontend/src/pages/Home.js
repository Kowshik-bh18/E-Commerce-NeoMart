import React, { useState, useEffect } from "react";
import {
  Box,
  Grid,
  Input,
  Select,
  Container,
  Heading,
  Text,
  Image,
  Button,
  useToast,
} from "@chakra-ui/react";
import { getProducts, getCategories, addToCart } from "../services/api";
import { Link } from "react-router-dom";

function Home() {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");
  const [searchQuery, setSearchQuery] = useState("");
  const toast = useToast();

  useEffect(() => {
    loadProducts();
    loadCategories();
  }, [selectedCategory, searchQuery]);

  const loadProducts = async () => {
    try {
      const data = await getProducts(selectedCategory, searchQuery);
      setProducts(data.results || []);
    } catch (error) {
      console.error("Error loading products:", error);
    }
  };

  const loadCategories = async () => {
    try {
      const data = await getCategories();
      setCategories(data.results || []);
    } catch (error) {
      console.error("Error loading categories:", error);
    }
  };

  const handleAddToCart = async (productId) => {
    try {
      await addToCart(productId, 1);
      toast({
        title: "Success",
        description: "Product added to cart",
        status: "success",
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      toast({
        title: "Error",
        description: error.response?.data?.error || "Failed to add to cart",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Container maxW="container.xl" py={8}>
      <Box mb={8}>
        <Input
          placeholder="Search products..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          mb={4}
        />
        <Select
          placeholder="Select category"
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
        >
          {categories.map((category) => (
            <option key={category.id} value={category.id}>
              {category.name}
            </option>
          ))}
        </Select>
      </Box>

      <Grid templateColumns="repeat(auto-fill, minmax(250px, 1fr))" gap={6}>
        {products.map((product) => (
          <Box
            key={product.id}
            borderWidth="1px"
            borderRadius="lg"
            overflow="hidden"
            p={4}
          >
            {product.image && (
              <Image src={product.image} alt={product.name} mb={4} />
            )}
            <Heading as="h3" size="md" mb={2}>
              <Link to={`/products/${product.id}`}>{product.name}</Link>
            </Heading>
            <Text mb={2}>${product.price}</Text>
            <Button
              colorScheme="blue"
              onClick={() => handleAddToCart(product.id)}
            >
              Add to Cart
            </Button>
          </Box>
        ))}
      </Grid>
    </Container>
  );
}

export default Home;

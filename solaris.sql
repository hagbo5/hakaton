-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-08-2025 a las 04:04:01
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `solaris`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajes_contacto`
--

CREATE TABLE `mensajes_contacto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mensaje` text NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mensajes_contacto`
--

INSERT INTO `mensajes_contacto` (`id`, `nombre`, `email`, `mensaje`, `fecha`) VALUES
(1, 'hugo ', 'hugo05bl2@gmail.com', 'quiero comprar al por mayor', '2025-08-10 19:36:52'),
(2, 'hugo ', 'hugo05bl2@gmail.com', 'quiero comprar al por mayor', '2025-08-10 19:43:42'),
(3, 'may', 'mmenamontagun@gmail.com', 'quiero regresar la compra', '2025-08-10 23:34:57'),
(4, 'may', 'mmenamontagun@gmail.com', 'quiero regresar la compra', '2025-08-10 23:36:14'),
(5, 'sol', 'sol@sol.com', 'sollllllllsdfdsfdsfsdfsf', '2025-08-13 00:17:39');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `disponible` enum('si','no') DEFAULT 'si',
  `foto` varchar(255) DEFAULT NULL,
  `seccion` varchar(20) DEFAULT 'ingenieria'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `descripcion`, `precio`, `cantidad`, `disponible`, `foto`, `seccion`) VALUES
(1, 'panel solar', 'es una panel aficiente ', 120000.00, 6, 'si', 'sol2.jpeg', 'solar'),
(2, 'kit Eólico', 'Planta eolica para casas ', 1000000.00, 10, 'si', 'elo1.jpg', 'eolico'),
(3, 'panel solar', 'Panel Solar Monocristalino 240W Tensite', 268000.00, 9, 'si', 'sol3.webp', 'solar'),
(4, 'Panel Solar Bifacial 610W Tipo N Tensite', 'El Panel Solar Bifacial 610W N-Type Tensite es una referencia de alta capacidad y rendimiento ', 750000.00, 10, 'si', 'sol4.webp', 'solar'),
(5, '	kit Eólico', 'mas potente', 2000000.00, 10, 'si', 'elo3.jpg', 'eolico'),
(6, 'Servicio Diseño e Ingeniería del Sistema', 'Con el servicio de diseño e ingeniería del sistema fotovoltaico, nuestro equipo de ingenieros se asegura de diseñar y planear un sistema eficiente', 142800.00, 8, 'si', 'diseno_ing.jpg', 'ingenieria'),
(7, 'Servicio Visita Técnica', 'El servicio de visita técnica a sistemas fotovoltaicos se lleva a cabo por técnicos o ingenieros expertos en energía solar,', 190000.00, 9, 'si', 'visita_tec.jpg', 'ingenieria'),
(9, 'Cargador_solar_celu', 'Cargadores para celulares que cargan haciendo uso de los rayos del sol', 320000.00, 11, 'si', 'cargador_solar.jpg', 'solar');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp(),
  `rol` varchar(20) DEFAULT 'usuario'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `username`, `email`, `password`, `telefono`, `direccion`, `fecha_registro`, `rol`) VALUES
(1, 'Admin', 'Solaris', 'admin', 'admin@solaris.com', 'scrypt:32768:8:1$Ebn444BJy38ZrjTz$f446d4eaa61fc368b995246dff41dde637f12767e2e26c78edc2346a6ace77157f455750bd89b86e8161624293326c91e8d25475f8cdac692f833a274a7f3ec7', '3104385467', 'calle 12 # 23-07', '2025-08-10 19:05:46', 'admin'),
(4, 'may dayana m m', 'mena', 'may', 'mmenamontagu@gmail.com', 'scrypt:32768:8:1$aLALiIHmUvXm8hGN$5e75ce683c6cab38b082f3778c3ca84c5ed6edb5f63ee7ffd8575d8fbd60e72cb3be1d52b8f9e4b8b345b01fd42ea19ab1dd635e23e3a1c57ec22f45682ddde2', '3244935093', 'calle 12 # 23-07', '2025-08-10 19:49:08', 'usuario'),
(5, 'pirry', 'cortina', 'ingpirry', 'pirryxtremo@gmail.com', 'scrypt:32768:8:1$vO8Ea15SEryCfRrN$095202397223b1e5b12b9e51941354b2e94a5381dc67e022f3dc83dffd5af673bd7a3666364966dfa0b6399f39cd29c7c231de39c7b8673ac68453fe6dbde0b8', '3046325748', NULL, '2025-08-10 23:42:21', 'admin'),
(6, 'JUAN', 'CANTILLO', 'SOYCRAZY', 'jjuancantillomr@gmai.com', 'scrypt:32768:8:1$9TtglBKUiTgFUmuG$182a8f0024249e4184c5323f50e3545f906fa9354014d9ab0040b934be5d299f42f2921bb9c19ed4adf947a89d7b362e880e6e4bfa6aa62c79885582e06b82a9', '3013548109', 'Calle 17a #29-88', '2025-08-10 23:45:39', 'usuario'),
(7, 'Milena ', 'Robles', 'nino', 'diannysmilenarobles@gmail.com', 'scrypt:32768:8:1$Cv3QveA6WNARg3C7$5ac215d3565ebdba4a59fd8f34a8825227da9963e0aa53161e570c7d2432433452fc6bc59625250299bc395d098b27bcc2baa7ed95394183621f64fc6b36d3f8', '3003212827', 'calle 24 # 6A-21 5noviembre', '2025-08-11 00:08:39', 'admin'),
(8, 'veterinaria', 'CANTILLO', 'hola ', 'jjuancantillomr@gmail.com', 'scrypt:32768:8:1$whPAqHAcYkGmD6pP$27d600e0d1ff548d954841ec55ba4c442ae88c14bbb9363ef213a1b1abdba7277c4ee1b93bbbb7c52e236eab3753bb85989bd27f90b4b242bab740092cb049bf', '3216549870', NULL, '2025-08-12 21:56:37', 'admin');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `nombre_cliente` varchar(100) DEFAULT NULL,
  `email_cliente` varchar(100) DEFAULT NULL,
  `telefono_cliente` varchar(30) DEFAULT NULL,
  `direccion_envio` varchar(255) DEFAULT NULL,
  `metodo_pago` varchar(50) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `fecha` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `usuario_id`, `nombre_cliente`, `email_cliente`, `telefono_cliente`, `direccion_envio`, `metodo_pago`, `total`, `fecha`) VALUES
(4, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 4796000.00, '2025-08-10 17:51:42'),
(5, 4, 'may dayana m m', 'mmenamontagu@gmail.com', '3244935093', 'calle 12 # 23-07', 'contraentrega', 3600000.00, '2025-08-10 18:06:09'),
(6, 4, 'may dayana m m', 'mmenamontagu@gmail.com', '3244935093', 'calle 12 # 23-07', 'contraentrega', 804000.00, '2025-08-10 18:31:55'),
(7, 6, 'JUAN', 'jjuancantillomr@gmai.com', '3013548109', 'Calle 17a #29-88', 'contraentrega', 1000000.00, '2025-08-10 18:47:32'),
(8, 7, 'Milena ', 'diannysmilenarobles@gmail.com', '3003212827', 'calle 24 # 6A-21 5noviembre', 'contraentrega', 388000.00, '2025-08-10 19:11:27'),
(9, 7, 'Milena ', 'diannysmilenarobles@gmail.com', '3003212827', 'calle 24 # 6A-21 5noviembre', 'tarjeta', 1000000.00, '2025-08-10 19:40:19'),
(10, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 120000.00, '2025-08-10 20:34:54'),
(11, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 360000.00, '2025-08-12 07:40:57'),
(12, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 120000.00, '2025-08-12 07:51:54'),
(13, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 1500000.00, '2025-08-12 08:18:32'),
(14, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 1500000.00, '2025-08-12 08:20:06'),
(15, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 1500000.00, '2025-08-12 08:21:01'),
(16, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 3000000.00, '2025-08-12 08:21:32'),
(17, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 240000.00, '2025-08-12 08:28:20'),
(18, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 410800.00, '2025-08-12 11:30:13'),
(19, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 120000.00, '2025-08-12 15:44:00'),
(20, 1, 'Admin', 'admin@solaris.com', '3104385467', 'calle 12 # 23-07', 'contraentrega', 120000.00, '2025-08-12 15:45:31');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta_detalles`
--

CREATE TABLE `venta_detalles` (
  `id` int(11) NOT NULL,
  `venta_id` int(11) DEFAULT NULL,
  `producto_id` int(11) DEFAULT NULL,
  `nombre_producto` varchar(100) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio_unitario` decimal(10,2) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `venta_detalles`
--

INSERT INTO `venta_detalles` (`id`, `venta_id`, `producto_id`, `nombre_producto`, `cantidad`, `precio_unitario`, `subtotal`) VALUES
(1, 4, 1, 'panel solar', 1, 1200000.00, 1200000.00),
(2, 4, 3, 'panel solar', 1, 268000.00, 268000.00),
(3, 4, 6, 'Servicio Diseño e Ingeniería del Sistema', 1, 1428000.00, 1428000.00),
(4, 4, 7, 'Servicio Visita Técnica', 1, 1900000.00, 1900000.00),
(5, 5, 1, 'panel solar', 3, 1200000.00, 3600000.00),
(6, 6, 3, 'panel solar', 3, 268000.00, 804000.00),
(7, 7, 2, 'kit Eólico', 1, 1000000.00, 1000000.00),
(8, 8, 1, 'panel solar', 1, 120000.00, 120000.00),
(9, 8, 3, 'panel solar', 1, 268000.00, 268000.00),
(10, 9, 2, 'kit Eólico', 1, 1000000.00, 1000000.00),
(11, 10, 1, 'panel solar', 1, 120000.00, 120000.00),
(12, 11, 1, 'panel solar', 3, 120000.00, 360000.00),
(13, 12, 1, 'panel solar', 1, 120000.00, 120000.00),
(14, 13, 4, 'Panel Solar Bifacial 610W Tipo N Tensite', 2, 750000.00, 1500000.00),
(15, 14, 4, 'Panel Solar Bifacial 610W Tipo N Tensite', 2, 750000.00, 1500000.00),
(16, 15, 4, 'Panel Solar Bifacial 610W Tipo N Tensite', 2, 750000.00, 1500000.00),
(17, 16, 4, 'Panel Solar Bifacial 610W Tipo N Tensite', 4, 750000.00, 3000000.00),
(18, 17, 1, 'panel solar', 2, 120000.00, 240000.00),
(19, 18, 6, 'Servicio Diseño e Ingeniería del Sistema', 1, 142800.00, 142800.00),
(20, 18, 3, 'panel solar', 1, 268000.00, 268000.00),
(21, 19, 1, 'panel solar', 1, 120000.00, 120000.00),
(22, 20, 1, 'panel solar', 1, 120000.00, 120000.00);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `mensajes_contacto`
--
ALTER TABLE `mensajes_contacto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `venta_detalles`
--
ALTER TABLE `venta_detalles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `venta_id` (`venta_id`),
  ADD KEY `producto_id` (`producto_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `mensajes_contacto`
--
ALTER TABLE `mensajes_contacto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `venta_detalles`
--
ALTER TABLE `venta_detalles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `venta_detalles`
--
ALTER TABLE `venta_detalles`
  ADD CONSTRAINT `venta_detalles_ibfk_1` FOREIGN KEY (`venta_id`) REFERENCES `ventas` (`id`),
  ADD CONSTRAINT `venta_detalles_ibfk_2` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

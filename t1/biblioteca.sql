-- phpMyAdmin SQL Dump
-- version 6.0.0-dev+20231114.4c382d3fa8
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-08-2025 a las 23:54:27
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ejemplares`
--

CREATE TABLE `ejemplares` (
  `id` int(11) NOT NULL,
  `libro_id` int(11) NOT NULL,
  `estanteria_id` int(11) DEFAULT NULL,
  `tipo` enum('fisico','digital') DEFAULT 'fisico',
  `estado` enum('disponible','prestado','reservado') DEFAULT 'disponible',
  `codigo_interno` varchar(20) DEFAULT NULL,
  `url_digital` varchar(255) DEFAULT NULL,
  `formato_digital` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ejemplares`
--

INSERT INTO `ejemplares` (`id`, `libro_id`, `estanteria_id`, `tipo`, `estado`, `codigo_interno`, `url_digital`, `formato_digital`) VALUES
(1, 1, 1, 'fisico', 'prestado', 'ECO-101', NULL, NULL),
(2, 1, 1, 'fisico', 'prestado', 'ECO-102', NULL, NULL),
(3, 2, NULL, 'digital', 'prestado', NULL, NULL, NULL),
(7, 1, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(8, 1, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(9, 1, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(10, 2, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(11, 2, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(12, 8, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(13, 8, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(14, 9, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(15, 9, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(16, 9, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(17, 10, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(18, 10, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(19, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(20, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(21, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(22, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(23, 1, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(24, 1, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(25, 1, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(26, 1, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(27, 1, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(28, 2, NULL, 'fisico', 'prestado', NULL, NULL, NULL),
(29, 2, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(30, 2, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(31, 2, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(32, 2, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(33, 8, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(34, 8, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(35, 8, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(36, 8, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(37, 8, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(38, 9, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(39, 9, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(40, 9, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(41, 9, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(42, 9, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(43, 10, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(44, 10, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(45, 10, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(46, 10, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(47, 10, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(48, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(49, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(50, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(51, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(52, 14, NULL, 'fisico', 'disponible', NULL, NULL, NULL),
(56, 23, NULL, 'fisico', 'prestado', 'LIB-23-001', NULL, NULL),
(58, 26, 1, 'fisico', 'prestado', 'LIB-26-001', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estanterias`
--

CREATE TABLE `estanterias` (
  `id` int(11) NOT NULL,
  `ubicacion` varchar(50) NOT NULL,
  `tema_principal` varchar(50) NOT NULL,
  `material` varchar(50) DEFAULT NULL,
  `capacidad_total` int(11) NOT NULL
) ;

--
-- Volcado de datos para la tabla `estanterias`
--

INSERT INTO `estanterias` (`id`, `ubicacion`, `tema_principal`, `material`, `capacidad_total`) VALUES
(1, 'Sección A - Fila 1', 'Economía', 'Madera', 2),
(2, 'Sección B - Fila 3', 'Ciencia', 'Metal', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int(11) NOT NULL,
  `codigo_estudiante` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id`, `codigo_estudiante`, `nombre`, `apellido`, `email`) VALUES
(1, 'U12345', 'Carlos', 'Gómez', 'carlos.gomez@uniandes.edu.co'),
(2, 'U67890', 'Ana', 'Suárez', 'ana.suarez@uniandes.edu.co'),
(3, 'U54321', 'Marta', 'Jiménez', 'marta.jimenez@uniandes.edu.co'),
(4, 'U98765', 'Pedro', 'Salazar', 'pedro.salazar@uniandes.edu.co'),
(5, 'U123312', 'Melani', 'Robles', 'Melani@uniandes.edu.co');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `id` int(11) NOT NULL,
  `isbn` varchar(20) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `anio_publicacion` int(11) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`id`, `isbn`, `titulo`, `anio_publicacion`, `categoria`, `autor`) VALUES
(1, '978-958-123456-1', 'Introducción a la Economía', 2012, 'Economía', 'Juan Pérez'),
(2, '978-958-987654-2', 'Ciencia para Todos', 2019, 'Ciencia', 'Laura Ríos'),
(8, '978-958-111111-1', 'Historia Universal', 2017, 'Historia', 'Luis Torres C'),
(9, '978-958-222222-2', 'Física Cuántica Básica', 2018, 'Ciencia', 'Ana Martínez'),
(10, '978-958-333333-3', 'Introducción a la Programación', 2022, 'Tecnología', 'Pedro Ramírez'),
(14, '978-958-333333-12121', 'Etica Moderna', 2025, 'Ciencia', 'Mateo Romero'),
(23, '978-9232323', 'Sociedad', 2022, 'Filosofia	', 'Lopez'),
(26, '101010101', 'Determinismo ', 2010, 'Filosofia	', 'Pluton');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `id` int(11) NOT NULL,
  `ejemplar_id` int(11) NOT NULL,
  `estudiante_id` int(11) NOT NULL,
  `fecha_prestamo` date NOT NULL,
  `fecha_devolucion_estimada` date NOT NULL,
  `fecha_devolucion_real` date DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`id`, `ejemplar_id`, `estudiante_id`, `fecha_prestamo`, `fecha_devolucion_estimada`, `fecha_devolucion_real`) VALUES
(8, 7, 2, '2025-08-15', '2025-08-19', NULL),
(9, 14, 2, '2025-08-15', '2025-08-17', NULL),
(11, 10, 1, '2025-08-12', '2025-08-12', NULL),
(12, 28, 1, '2025-08-15', '2025-08-21', NULL),
(15, 23, 1, '2025-08-15', '2025-08-18', NULL),
(16, 56, 2, '2025-08-15', '2025-08-26', NULL),
(18, 11, 4, '2025-08-13', '2025-08-19', NULL),
(19, 2, 1, '2025-08-15', '2025-08-18', NULL);

--
-- Disparadores `prestamos`
--
DELIMITER $$
CREATE TRIGGER `trg_prestamo_insert` AFTER INSERT ON `prestamos` FOR EACH ROW BEGIN
    UPDATE ejemplares
    SET estado = 'prestado'
    WHERE id = NEW.ejemplar_idDELIMITER ;
DELIMITER $$
CREATE TRIGGER `trg_prestamo_update` AFTER UPDATE ON `prestamos` FOR EACH ROW BEGIN
    IF NEW.fecha_devolucion_real IS NOT NULL THEN
        UPDATE ejemplares
        SET estado = 'disponible'
        WHERE id = NEW.ejemplar_idDELIMITER ;

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_libros_prestados`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_libros_prestados` (
`titulo` varchar(100)
,`codigo_interno` varchar(20)
,`nombre` varchar(50)
,`apellido` varchar(50)
,`fecha_prestamo` date
,`fecha_devolucion_estimada` date
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_libros_prestados`
--
DROP TABLE IF EXISTS `vista_libros_prestados`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_libros_prestados`  AS SELECT `l`.`titulo` AS `titulo`, `e`.`codigo_interno` AS `codigo_interno`, `es`.`nombre` AS `nombre`, `es`.`apellido` AS `apellido`, `p`.`fecha_prestamo` AS `fecha_prestamo`, `p`.`fecha_devolucion_estimada` AS `fecha_devolucion_estimada` FROM (((`prestamos` `p` join `ejemplares` `e` on(`p`.`ejemplar_id` = `e`.`id`)) join `libros` `l` on(`e`.`libro_id` = `l`.`id`)) join `estudiantes` `es` on(`p`.`estudiante_id` = `es`.`id`)) WHERE `p`.`fecha_devolucion_real` is null ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ejemplares`
--
ALTER TABLE `ejemplares`
  ADD PRIMARY KEY (`id`),
  ADD KEY `estanteria_id` (`estanteria_id`),
  ADD KEY `idx_ejemplares_estado` (`estado`),
  ADD KEY `ejemplares_ibfk_1` (`libro_id`);

--
-- Indices de la tabla `estanterias`
--
ALTER TABLE `estanterias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_estudiante` (`codigo_estudiante`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `isbn` (`isbn`),
  ADD KEY `idx_libros_titulo` (`titulo`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `estudiante_id` (`estudiante_id`),
  ADD KEY `idx_prestamos_abiertos` (`ejemplar_id`,`fecha_devolucion_real`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ejemplares`
--
ALTER TABLE `ejemplares`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT de la tabla `estanterias`
--
ALTER TABLE `estanterias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `libros`
--
ALTER TABLE `libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ejemplares`
--
ALTER TABLE `ejemplares`
  ADD CONSTRAINT `ejemplares_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `ejemplares_ibfk_2` FOREIGN KEY (`estanteria_id`) REFERENCES `estanterias` (`id`);

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `prestamos_ibfk_1` FOREIGN KEY (`ejemplar_id`) REFERENCES `ejemplares` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `prestamos_ibfk_2` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
